import { Component, Input, Output, OnInit, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {
  @Input() placeholder: string = 'Find great recipes here...';
  @Output() searchChanged = new EventEmitter<string>();
  searchQuery: string = '';

  constructor() { }

  ngOnInit(): void {
  }

  onSearchClick() {
    if (this.searchQuery.trim() !== '') {
      this.searchChanged.emit(this.searchQuery);
    }
  }
}
