import React from 'react';
import { Tabs, TabsList, TabsTrigger, TabsContent } from "../components/ui/tabs";

const steps = [
  { value: 'step1', label: '步骤一' },
  { value: 'step2', label: '步骤二' },
  { value: 'step3', label: '步骤三' },
  { value: 'finish', label: '完成' },
];

const Performance: React.FC = () => {
  return (
    <div style={{ width: '100%', padding: '40px 0' }}>
      <Tabs defaultValue={steps[0].value}>
        <TabsList>
          {steps.map((step) => (
            <TabsTrigger key={step.value} value={step.value}>
              {step.label}
            </TabsTrigger>
          ))}
        </TabsList>
        <TabsContent value="step1">这里是步骤一的内容</TabsContent>
        <TabsContent value="step2">这里是步骤二的内容</TabsContent>
        <TabsContent value="step3">这里是步骤三的内容</TabsContent>
        <TabsContent value="finish">流程已完成！</TabsContent>
      </Tabs>
    </div>
  );
};

export default Performance;
