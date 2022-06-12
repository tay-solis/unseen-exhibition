import React from "react";

const Photo = (props) => {
  const { photo } = props;
  return (
    <div className="g-photo">
      <img className="g-photo__image" src={`${photo.photo}`} />
      <div className="g-photo__info">
        {photo.url ? (
          <a href={`${photo.url}`} target="_blank">
            <h2 className="g-photo__title">{photo.name}</h2>
          </a>
        ) : (
          <h2 className="g-photo__title">{photo.name}</h2>
        )}

        {photo.description && (
          <p className="g-photo__description">{photo.description}</p>
        )}
      </div>
    </div>
  );
};

export default Photo;
