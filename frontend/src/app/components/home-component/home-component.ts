import { Component } from '@angular/core';
import { HomeToolbarComponent } from '../home-toolbar-component/home-toolbar-component';
import { HomeFeatureComponent } from '../home-feature-component/home-feature-component';
import { LoginForm } from '../login-form/login-form';
import { SignupForm } from '../signup-form/signup-form';

@Component({
  selector: 'app-home-component',
  imports: [HomeToolbarComponent, HomeFeatureComponent, LoginForm, SignupForm],
  templateUrl: './home-component.html',
  styleUrl: './home-component.css',
})
export class HomeComponent {
  state: 'login' | 'signup' | 'loading' = 'login';

  toggleLogin(){
    this.state = 'login'
  }

  toggleSignup(){
    this.state = 'signup'
  }
}
