import React from 'react';
import './Hello.css';



class Hello extends React.Component {
    render() {
        return (



            <div className='Hello'>
                <h1>Bok</h1>
                <p>{this.props.greeting}</p>

            </div>
        )
    }
}

export default Hello;