import React from "react";
import { Link } from "react-router-dom";

const Photo = (props) => {
  const { photo } = props;
  return (
    <article className="g-photo">
      <Link to={`/gallery/${photo.slug}/`}>
        {photo.social_image ? 
        <img className="g-photo__image" src={`${photo.social_image}`} />
        :
        <img className="g-photo__image" src={`${photo.photo}`} />
        }
        
      </Link>

      <div className="g-photo__info">
        <Link to={`/gallery/${photo.slug}/`}>
          <h2 className="g-photo__title">{photo.name}</h2>
        </Link>

        {photo.description && (
          <p className="g-photo__description">{photo.description}</p>
        )}
      </div>
    </article>
  );
};

export default Photo;
