import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Vacancies() {
    const [vacancies, setVacancies] = useState([]);

    useEffect(() => {
        axios.get('/api/vacancies/')
            .then(response => {
                setVacancies(response.data);
            })
            .catch(error => {
                console.error('There was an error fetching the vacancies!', error);
            });
    }, []);

    return (
        <div>
            <h1>Vacancies</h1>
            <ul>
                {vacancies.map(vacancy => (
                    <li key={vacancy.id}>{vacancy.title} - {vacancy.company}</li>
                ))}
            </ul>
        </div>
    );
}

export default Vacancies;
