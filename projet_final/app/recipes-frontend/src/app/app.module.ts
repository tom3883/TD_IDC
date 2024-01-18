import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { RecipesComponent } from './recipes/recipes.component';
import { HttpClientModule } from '@angular/common/http';
import { SearchComponent } from './search/search.component';
import { FormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    RecipesComponent,
    SearchComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
  ],
  
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
