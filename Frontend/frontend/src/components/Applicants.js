import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Applicants() {
    const [applicants, setApplicants] = useState([]);

    useEffect(() => {
        axios.get('/api/applicants/')
            .then(response => {
                setApplicants(response.data);
            })
            .catch(error => {
                console.error('There was an error fetching the applicants!', error);
            });
    }, []);

    return (
        <div>
            <h1>Applicants</h1>
            <ul>
                {applicants.map(applicant => (
                    <li key={applicant.id}>{applicant.name} {applicant.surname}</li>
                ))}
            </ul>
        </div>
    );
}

export default Applicants;
