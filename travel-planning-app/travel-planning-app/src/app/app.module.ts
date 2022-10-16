import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from "@angular/common/http";

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FormsModule } from '@angular/forms';
import { RouteSearchComponent } from './route-search/route-search.component';
import { TripComponent } from './trip/trip.component';
import { GoogleMapsModule } from '@angular/google-maps';
import { LoadingPageComponent } from './loading-page/loading-page.component';

@NgModule({
  declarations: [
    AppComponent,
    RouteSearchComponent,
    TripComponent,
    LoadingPageComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    GoogleMapsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
