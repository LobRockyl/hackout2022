import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { RouteSearch } from 'RouteSearch';
import { TripApiService } from '../trip-api.service';

@Component({
  selector: 'app-route-search',
  templateUrl: './route-search.component.html',
  styleUrls: ['./route-search.component.css']
})
export class RouteSearchComponent implements OnInit {

  constructor(private tripApiService: TripApiService, private _router: Router) { }

  ngOnInit(): void {
  }

  findTrips(routeSearch: RouteSearch) {
    this.tripApiService.findTrips(routeSearch).subscribe(
      data => {
        console.log(data)
        this._router.navigate(['/results'])
      }

    )
  }
}
