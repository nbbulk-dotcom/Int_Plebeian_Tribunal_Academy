/**
 * International Plebeian Academy - System Health Chart
 * @author International Plebeian Academy Development Team
 * @license MIT
 * @version 1.0.0
 */

import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

interface SystemHealthChartProps {
  data?: any[];
}

const SystemHealthChart: React.FC<SystemHealthChartProps> = ({ data = [] }) => {
  const defaultData = [
    { time: '00:00', cpu: 45, memory: 60, network: 30 },
    { time: '04:00', cpu: 52, memory: 65, network: 35 },
    { time: '08:00', cpu: 68, memory: 72, network: 48 },
    { time: '12:00', cpu: 75, memory: 78, network: 55 },
    { time: '16:00', cpu: 62, memory: 70, network: 42 },
    { time: '20:00', cpu: 48, memory: 62, network: 38 },
  ];

  const chartData = data.length > 0 ? data : defaultData;

  return (
    <ResponsiveContainer width="100%" height={300}>
      <LineChart data={chartData}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="time" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="cpu" stroke="#8884d8" name="CPU %" />
        <Line type="monotone" dataKey="memory" stroke="#82ca9d" name="Memory %" />
        <Line type="monotone" dataKey="network" stroke="#ffc658" name="Network %" />
      </LineChart>
    </ResponsiveContainer>
  );
};

export default SystemHealthChart;
