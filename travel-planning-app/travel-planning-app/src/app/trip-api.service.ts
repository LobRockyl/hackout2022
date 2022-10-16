import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { RouteSearch } from 'RouteSearch';

@Injectable({
  providedIn: 'root'
})
export class TripApiService {

  constructor(private _tripHttpClient:HttpClient) { }

  TRIP_API_URL = " "

  findTrips(routeSearch:RouteSearch):Observable<any>{

    return this._tripHttpClient.post<any>(this.TRIP_API_URL,routeSearch)
    
  }
}
