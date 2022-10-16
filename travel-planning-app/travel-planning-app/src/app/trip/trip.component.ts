import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { TripApiService } from '../trip-api.service';

@Component({
  selector: 'app-trip',
  templateUrl: './trip.component.html',
  styleUrls: ['./trip.component.css']
})
export class TripComponent implements OnInit {

  petrolPumpList:Array<any> = []

  restrauntList:Array<any> = []

  constructor(private tripApiService:TripApiService, private _router:Router) { }

  ngOnInit(): void {
  }

}
