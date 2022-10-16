export class RouteSearch{
    constructor(public vehicleType?:string,
                public fromLocation?:string, 
                public toLocation?:string,
                public timeStamp?: Date
               ){}
}