import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';
import TestWrapper from './test-utils';

test('renders App component and checks for content', () => {
  render(
    <TestWrapper>
      <App />
    </TestWrapper>
  );
  expect(screen.getByText(/Data Parser Portal/i)).toBeInTheDocument();
});
