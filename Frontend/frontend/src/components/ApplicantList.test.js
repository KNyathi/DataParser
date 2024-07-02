import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import axios from 'axios';
import ApplicantList from '../ApplicantList';

jest.mock('axios');

const mockApplicants = [
  {
    id: 1,
    title: 'John Doe',
    link: 'http://example.com',
    age: '30',
    status: 'Employed',
    experience_duration: '5 years',
    last_employer: 'Example Corp',
    last_position: 'Software Engineer',
    employment_dates: '2015-2020'
  }
];

test('renders applicant list and checks for applicants', async () => {
  axios.get.mockResolvedValue({ data: mockApplicants });

  render(<ApplicantList />);

  expect(screen.getByText(/Applicants/i)).toBeInTheDocument();

  await waitFor(() => {
    expect(screen.getByText('John Doe')).toBeInTheDocument();
    expect(screen.getByText('30')).toBeInTheDocument();
    expect(screen.getByText('Employed')).toBeInTheDocument();
    expect(screen.getByText('5 years')).toBeInTheDocument();
    expect(screen.getByText('Example Corp')).toBeInTheDocument();
    expect(screen.getByText('Software Engineer')).toBeInTheDocument();
    expect(screen.getByText('2015-2020')).toBeInTheDocument();
  });
});
