/**
 * International Plebeian Academy - Bot Performance Chart
 * @author International Plebeian Academy Development Team
 * @license MIT
 * @version 1.0.0
 */

import React from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

interface BotPerformanceChartProps {
  data?: any[];
}

const BotPerformanceChart: React.FC<BotPerformanceChartProps> = ({ data = [] }) => {
  const defaultData = [
    { division: 'Communications', tasks: 42, success: 95 },
    { division: 'Human Dev', tasks: 38, success: 92 },
    { division: 'Support', tasks: 45, success: 97 },
    { division: 'Action', tasks: 51, success: 94 },
    { division: 'Integrity', tasks: 35, success: 98 },
    { division: 'Membership', tasks: 40, success: 93 },
    { division: 'Strategic', tasks: 33, success: 96 },
  ];

  const chartData = data.length > 0 ? data : defaultData;

  return (
    <ResponsiveContainer width="100%" height={300}>
      <BarChart data={chartData}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="division" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Bar dataKey="tasks" fill="#8884d8" name="Tasks Completed" />
        <Bar dataKey="success" fill="#82ca9d" name="Success Rate %" />
      </BarChart>
    </ResponsiveContainer>
  );
};

export default BotPerformanceChart;
