import { Routes } from '@angular/router';
import { HomeComponent } from './components/home-component/home-component';
import { NotFoundComponent } from './components/not-found-component/not-found-component';

export const routes: Routes = [
    { path: 'home', component: HomeComponent },
    { path: '', redirectTo: 'home', pathMatch: 'full' },
    { path: '404', component: NotFoundComponent },
    { path: '**', redirectTo: '404', pathMatch: 'full'}
];
