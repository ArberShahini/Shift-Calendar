import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-home-feature-component',
  imports: [],
  templateUrl: './home-feature-component.html',
  styleUrl: './home-feature-component.css',
})
export class HomeFeatureComponent {
  @Input() header: string = '';
  @Input() description: string = '';
}
