import { Component, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-login-form',
  imports: [],
  templateUrl: './login-form.html',
  styleUrl: './login-form.css',
})
export class LoginForm {
  @Output() signupClicked = new EventEmitter<void>();

  onSignupClick() {
    this.signupClicked.emit();
  }
}
