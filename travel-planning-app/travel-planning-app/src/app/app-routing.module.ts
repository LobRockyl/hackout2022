import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoadingPageComponent } from './loading-page/loading-page.component';
import { RouteSearchComponent } from './route-search/route-search.component';
import { TripComponent } from './trip/trip.component';

const routes: Routes = [
  {
    path:'search',component:RouteSearchComponent
  },
  {
    path:'results',component:TripComponent
  },
  {
    path:'**', redirectTo:'/search'
  },
  {
    path:'loading', component:LoadingPageComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
