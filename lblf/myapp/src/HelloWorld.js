import React, { useState, useEffect } from 'react';
import axios from 'axios';

function HelloWorld() {
    const [message, setMessage] = useState('');

    useEffect(() => {
        axios.get('http://localhost:8000/api/hello-world/')
            .then(response => {
                setMessage(response.data.message);
            })
            .catch(error => {
                console.log(error);
            });
    }, []);

    return (
        <div>
            <h1 className="text-2xl w-100 text-center font-bold">Hi there!</h1>
            <p>{message}</p>
        </div>
    );
}

export default HelloWorld;