import { Component } from '@angular/core';

@Component({
  selector: 'app-signup-form',
  imports: [],
  templateUrl: './signup-form.html',
  styleUrl: './signup-form.css',
})
export class SignupForm {
  currentStep: number = 1;

  next() {
    if(this.currentStep < 4)
    this.currentStep++;
  }

  prev() {
    this.currentStep--;
  }
}
