import { Component } from '@angular/core';
import { HomeToolbarComponent } from '../home-toolbar-component/home-toolbar-component';
import { HomeFeatureComponent } from '../home-feature-component/home-feature-component';

@Component({
  selector: 'app-home-component',
  imports: [HomeToolbarComponent, HomeFeatureComponent],
  templateUrl: './home-component.html',
  styleUrl: './home-component.css',
})
export class HomeComponent {}
