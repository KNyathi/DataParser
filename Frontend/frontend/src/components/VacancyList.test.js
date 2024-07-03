import React from 'react';
import { render, screen } from '@testing-library/react';
import axios from 'axios';
import VacancyList from './VacancyList';
import TestWrapper from '../test-utils';
import { act } from 'react'; // Import act from react-dom/test-utils

jest.mock('axios');

const mockVacancies = [
  {
    id: 1,
    title: 'Python Developer',
    compensation: '1000 USD',
    experience: '2 years',
    employer: 'Example Corp',
    location: 'New York'
  }
];

test('renders vacancy list and checks for vacancies', async () => {
  axios.get.mockResolvedValue({ data: mockVacancies });

  await act(async () => {
    render(
      <TestWrapper>
        <VacancyList />
      </TestWrapper>
    );
  });

  expect(screen.getByText('Python Developer')).toBeInTheDocument();
  expect(screen.getByText('1000 USD')).toBeInTheDocument();
  expect(screen.getByText('2 years')).toBeInTheDocument();
  expect(screen.getByText('Example Corp')).toBeInTheDocument();
  expect(screen.getByText('New York')).toBeInTheDocument();
});
