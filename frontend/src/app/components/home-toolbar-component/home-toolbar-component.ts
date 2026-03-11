import { Component, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-home-toolbar-component',
  imports: [],
  templateUrl: './home-toolbar-component.html',
  styleUrl: './home-toolbar-component.css',
})
export class HomeToolbarComponent {
  @Output() loginClicked = new EventEmitter<void>();
  @Output() signupClicked = new EventEmitter<void>();

  onLoginClick() {
    this.loginClicked.emit();
  }

  onSignupClick() {
    this.signupClicked.emit();
  }
}
