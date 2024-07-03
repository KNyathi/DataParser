import React from 'react';
import { render, screen } from '@testing-library/react';
import Analytics from './Analytics';
import TestWrapper from '../test-utils';

test('renders analytics component and checks for content', () => {
  render(
    <TestWrapper>
      <Analytics />
    </TestWrapper>
  );
  expect(screen.getByText(/We have/i)).toBeInTheDocument();
});
