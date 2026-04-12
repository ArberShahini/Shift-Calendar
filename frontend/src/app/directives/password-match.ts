import { Directive } from '@angular/core';
import { AbstractControl, NG_VALIDATORS, ValidationErrors, Validator } from '@angular/forms';

@Directive({
  selector: '[passwordMatch]',
  providers: [{ provide: NG_VALIDATORS, useExisting: PasswordMatch, multi: true }]
})
export class PasswordMatch implements Validator{
  validate(control: AbstractControl): ValidationErrors | null {
    const password = control.get('password');
    const confirmPassword = control.get('confirmPassword');

    if (password && confirmPassword && password.value !== confirmPassword.value) {
      return { passwordMatch: true };
    }
    return null;
  }
}
