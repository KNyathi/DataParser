import React from 'react';
import { render, screen } from '@testing-library/react';
import axios from 'axios';
import ApplicantList from './ApplicantList';
import TestWrapper from '../test-utils';
import { act } from 'react'; 

jest.mock('axios');

const mockApplicants = [
  {
    id: 1,
    title: 'John Doe',
    age: '30',
    status: 'Employed',
    experience_duration: '5 years',
    last_employer: 'Example Corp',
    last_position: 'Software Engineer'
  }
];

test('renders applicant list and checks for applicants', async () => {
  axios.get.mockResolvedValue({ data: mockApplicants });

  await act(async () => {
    render(
      <TestWrapper>
        <ApplicantList />
      </TestWrapper>
    );
  });

  expect(screen.getByText('Applicants')).toBeInTheDocument();
  expect(screen.getByText('John Doe')).toBeInTheDocument();
  expect(screen.getByText('30')).toBeInTheDocument();
  expect(screen.getByText('Employed')).toBeInTheDocument();
  expect(screen.getByText('5 years')).toBeInTheDocument();
  expect(screen.getByText('Example Corp')).toBeInTheDocument();
  expect(screen.getByText('Software Engineer')).toBeInTheDocument();
});
