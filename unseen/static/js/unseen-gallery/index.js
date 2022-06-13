import React from "react";
import ReactDOM from "react-dom/client";
import GalleryRouter from "./GalleryRouter";

const e = React.createElement;

const domContainer = document.querySelector('#gallery');
const root = ReactDOM.createRoot(domContainer);
root.render(e(GalleryRouter));
