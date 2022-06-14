import React from "react";

import Photo from "./Photo";

function Photos(props) {
  const { photos, currentIndex } = props;

  let photoComponents = photos.map((photo, i) => {
    return <Photo key={i} photo={photo} />;
  });

  return (
    <section
      className="gallery__photos"
      style={{ transform: `translateX(-${currentIndex * (100 / 3)}%)` }}
    >
      {photoComponents}
    </section>
  );
}

export default Photos;
