import { Component, input, Input } from '@angular/core';

@Component({
  selector: 'app-error-card-component',
  imports: [],
  templateUrl: './error-card-component.html',
  styleUrl: './error-card-component.css',
})
export class ErrorCardComponent {
  @Input() header: string = ''
  @Input() message: string = ''
}
