import { Injectable } from "@angular/core";
import { HttpClient, HttpHeaders, HttpParams } from "@angular/common/http";
import { Observable } from "rxjs";
import { environment } from "../../environments/environment";

export interface RequestOptions {
    headers?: { [key: string]: string };
    params?: { [key: string]: string };
    body?: any;
}

@Injectable({
    providedIn: 'root'
})
export class RequestService {
    private baseUrl = environment.apiUrl;

    constructor(private http: HttpClient){}

    makeRequest<T>(method: string, endpoint: string, options?: RequestOptions): Observable<T>{
        const url = `${this.baseUrl}${endpoint}`;
        const headers = new HttpHeaders(options?.headers || {});
        const params = new HttpParams(options?.params || {});

        return this.http.request<T>(method, url, {
            headers,
            params,
            body: options?.body
        });
    }
}