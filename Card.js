import React from 'react';

const Card = ({ name, id }) => {
    const Random = (Math.floor(Math.random() * 1000) + 1)
    return (

        <div className='tc bg-light-blue dib br3 pa3 ma2 grow bw2 shadow-5'>

            <img alt='robots' src={`https://robohash.org/${Random + name.toLowerCase()}?size=280x226`} />
            <div>
                <h2 className='f3 font-family: avenir'>{name}</h2>
                <p>{Random}</p>
            </div>
        </div>
    );
}

export default Card;