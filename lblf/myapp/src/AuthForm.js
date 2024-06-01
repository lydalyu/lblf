import React, { useState, useEffect } from 'react';
import * as utils from './util.js';

function AuthForm() {
    const [message, setMessage] = useState('');
    var [form_action, setFormAction] = useState('login');

    useEffect(() => {
        document.title = "Login";
    }, []);

    function toggleForm() {
        document.title = form_action == 'login' ? 'Register' : 'Login';
        setFormAction((form_action == 'login' ? 'register' : 'login'));
    }

    function sendForm(form_action, event) {
        event.preventDefault();
        let form = event.target;
        let form_data = new FormData(form);
        
        fetch('/api/' + form_action, {
            headers: { "X-CSRFToken": utils.getCookie('csrftoken') },
            method: 'POST',
            body: form_data,
        })
            .then(response => response.json())
            .then(result => {
                console.log(result);
            });
    }

    return (
        <form className='form' onSubmit={(event) => { sendForm(form_action, event)}} method="POST">
            <h4 className='text-lg w-100 text-center font-bold mb-8'>Please, {form_action} here!</h4>
            <div className='form-block-2'>
                <label for="email">Email: </label>
                <input className='input' id="email" type="email" name="email" />
            </div>
            <div className='form-block-2'>
                <label for="password">Password: </label>
                <input className='input' id="password" type="password" name="password" />
            </div>
            {   form_action == 'register' &&
                <div className='form-block-2'>
                    <label for="password_confirm">Password: </label>
                    <input className='input' id="password_confirm" type="password" name="password_confirm" />
                </div>
            }
            <div className='my-2 text-right text-sm text-blue-800'>
                <span className='cursor-pointer' onClick={toggleForm}>{form_action=='login' ? 'Register' : 'Login' } form</span>
            </div>
            <div className='w-100 form-block mb-0'>
                <button className='button capitalize' type="submit">{ form_action }</button>
            </div>
        </form>
    );
}

export default AuthForm;