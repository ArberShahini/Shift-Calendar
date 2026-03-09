import { Component } from '@angular/core';
import { HomeToolbarComponent } from '../home-toolbar-component/home-toolbar-component';
import { HomeFeatureComponent } from '../home-feature-component/home-feature-component';
import { LoginForm } from '../login-form/login-form';

@Component({
  selector: 'app-home-component',
  imports: [HomeToolbarComponent, HomeFeatureComponent, LoginForm],
  templateUrl: './home-component.html',
  styleUrl: './home-component.css',
})
export class HomeComponent {
  activeForm: 'login' | 'signup' = 'login';
}
