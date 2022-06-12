import React from "react";

import Photos from "./components/Photos";

export default class Gallery extends React.Component {
  render() {
    return (
      <div className="gallery__container">
        <Photos />

        <section className="gallery__continue">
          <a href="/conversation/">
            <button className="button gallery__continue-button">
              Continue
            </button>
          </a>
        </section>
      </div>
    );
  }
}
