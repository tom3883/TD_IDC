import { Component, Output, OnInit, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {
  @Output() searchChanged = new EventEmitter<string>();
  searchQuery: string = '';

  constructor() { }

  ngOnInit(): void {
  }

  onSearch() {
    this.searchChanged.emit(this.searchQuery);
  }
}
