import { Directive } from '@angular/core';
import { AbstractControl, NG_VALIDATORS, ValidationErrors, Validator } from '@angular/forms';

@Directive({
  selector: '[passwordValidator]',
  providers: [{ provide: NG_VALIDATORS, useExisting: PasswordValidator, multi: true }]
})
export class PasswordValidator implements Validator{
  validate(control: AbstractControl): ValidationErrors | null {
    const password = control.get('password');
    if (!password || !password.value) return null;

    const value = password.value;
    const errors: ValidationErrors = {}

    if (value.length < 8) {
      errors['minLength'] = true;
    }
    if (!/[A-Z]/.test(value)) {
      errors['missingUppercase'] = true;
    }
    if (!/[0-9]/.test(value)) {
      errors['missingDigit'] = true;
    }
    
    return Object.keys(errors).length > 0 ? { passwordValidator: errors } : null;
  }
}