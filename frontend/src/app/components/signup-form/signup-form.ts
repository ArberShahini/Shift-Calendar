import { Component, ChangeDetectorRef, NgModule, ViewChild } from '@angular/core';
import { FormsModule, NgForm } from '@angular/forms';
import { RequestService } from '../../standalone_services/request-service';
import { environment } from '../../../environments/environment';
import { Company } from '../../models/company.model';
import { WorkProfile } from '../../models/work_profiles.model';
import { LoadingComponent } from '../loading-component/loading-component';
import { HttpErrorResponse } from '@angular/common/http';
import { ErrorCardComponent } from '../error-card-component/error-card-component';
import { PasswordMatch } from '../../directives/password-match';
import { PasswordValidator } from '../../directives/password-validator';
import { delay, flatMap } from 'rxjs';

@Component({
  selector: 'app-signup-form',
  imports: [LoadingComponent, FormsModule, ErrorCardComponent, PasswordMatch, PasswordValidator],
  templateUrl: './signup-form.html',
  styleUrl: './signup-form.css',
})
export class SignupForm {
  apiUrl = environment.apiUrl;

  currentStep: number = 1;
  isLoading: boolean = false;

  companies: Company[] = [];
  companiesSearchTerm: string = '';
  filteredCompanies: Company[] = [];
  noCompanies: boolean = false;
  selectedCompany: number = 0;
  companyFetchHasError: boolean = false;
  
  workProfiles: WorkProfile[] = [];
  workProfilesSearchTerm: string = '';
  filteredWorkProfiles: WorkProfile[] = [];
  noWorkProfiles: boolean = false;
  selectedWorkProfile: number = 0;
  workProfileFetchHasError: boolean = false;

  // CREDENTIALS FORM VARIABLES
  @ViewChild('credentialsForm') credentialsForm!: NgForm;
  firstName: string = '';
  lastName: string = '';
  email: string = '';
  password: string = '';
  confirmPassword: string = '';
  
  constructor(private requestService: RequestService, private cdr: ChangeDetectorRef) {}

  isCredentialsInvalid(): boolean {
    return this.credentialsForm ? this.credentialsForm.invalid ?? true : true;
  }

  changeStep(direction: string) {
    if ((this.currentStep == 1 && direction === 'next') || (this.currentStep == 3 && direction === 'prev')) {
      this.loadCompanies();
    }
    if ((this.currentStep == 2 && direction === 'next')) {
      this.loadWorkProfiles(this.selectedCompany);
    }
    if(this.currentStep < 4 && direction === 'next') {
      this.currentStep++;
    }
    if(this.currentStep > 1 && direction === 'prev') {
      this.currentStep--;
    }
  }
  
  onCompanyClick(id: number) {
    this.selectedCompany = id;
  }

  onWorkProfileClick(id: number) {
    this.selectedWorkProfile = id;
  }

  onNoCompanyChange(event: Event) {
    const checked = (event.target as HTMLInputElement).checked;
    if (checked) {
        this.selectedCompany = 0;
      }
  }
  
  loadCompanies() {
    this.isLoading = true;
    this.requestService.makeRequest<Company[]>('GET', '/api/companies')
    .subscribe({
      next: (response) => {
        this.companies = response;
        this.companyFetchHasError = false;
        this.isLoading = false;
        this.onCompaniesSearch('');
      },
      error: (error: HttpErrorResponse) => {
        if(error.status === 0) {
          this.companyFetchHasError = true;
          this.companies = [];
          this.filteredCompanies = [];
        }
        this.isLoading = false;
        this.cdr.detectChanges();
      }
    })
  }

  loadWorkProfiles(company_id: number) {
    this.isLoading = true;
    this.requestService.makeRequest<WorkProfile[]>('GET', `/api/workProfiles/getByCompanyId/${company_id}`)
    .subscribe({
      next: (response) => {
        this.workProfiles = response;
        this.workProfileFetchHasError = false;
        this.isLoading = false;
        this.onWorkProfilesSearch('');
      },
      error: (error: HttpErrorResponse) => {
        if(error.status === 0) {
          this.workProfileFetchHasError = true;
          this.workProfiles = [];
          this.filteredWorkProfiles = [];
        }
        this.isLoading = false;
        this.cdr.detectChanges();
      }
    })
  }

  fetchLogoUrl(path: string): string {
    return this.apiUrl + path;
  }

  parseHours(start_time: string) {
    let [hours, minutes] = start_time.split(':');
    return `${hours}:${minutes}`
  }

  addHours(start_time: string, daily_hours: number | string) {
    const [hoursStr, minutesStr] = start_time.split(":");
    const hours = parseInt(hoursStr, 10);
    const minutes = parseInt(minutesStr, 10);

    const additionalHours = typeof daily_hours === "string" ? parseFloat(daily_hours) : daily_hours;

    const totalMinutes = minutes + Math.round((additionalHours % 1) * 60);
    let newMinutes = totalMinutes % 60;
    let newHours = (hours + Math.floor(additionalHours) + Math.floor(totalMinutes / 60)) % 24;

    return `${newHours.toString().padStart(2, "0")}:${newMinutes.toString().padStart(2, "0")}`;
  }

  onWorkProfilesSearch(term: string) {
    this.companiesSearchTerm = term;
    this.filteredWorkProfiles = this.workProfiles.filter(wp =>
      wp.job_title.toLowerCase().includes(term.toLowerCase())
    );

    this.noWorkProfiles = this.filteredWorkProfiles.length === 0;
    console.log("Length: " + this.filteredWorkProfiles.length)
    console.log(this.filteredWorkProfiles)

    this.cdr.detectChanges();
  }

  onCompaniesSearch(term: string) {
    this.workProfilesSearchTerm = term;
    this.filteredCompanies = this.companies.filter(wp =>
      wp.name.toLowerCase().includes(term.toLowerCase())
    );

    this.noCompanies = this.filteredCompanies.length === 0;

    this.cdr.detectChanges();
  }
}