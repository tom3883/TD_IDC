import { Product } from "./product";

export interface Recipe {
    recipeName : string ;
    category : string ;
    ingredients : Array<string>[] ;
    products : Array<Product> ;
}