import React from "react";
import ReactDOM from "react-dom";
import Gallery from "./Gallery";

const e = React.createElement;

const domContainer = document.querySelector('#gallery');
const root = ReactDOM.createRoot(domContainer);
root.render(e(Gallery));
