import {Tabs, TabsList, TabsContent, TabsTrigger} from '@/components/ui/tabs'
import { Boxes, Play } from 'lucide-react'
import Performance from "@/components/Performance";


function App() {


  return (
    <div className="min-h-screen bg-gray-50 flex flex-col">
      <Tabs defaultValue="apps" className="w-full">
        <div className="sticky top-0 z-10 bg-white shadow">
          <div className="flex items-center px-4">
            <TabsList className="h-12 p-0 bg-white border-b rounded-none sticky top-12 z-10">
              <TabsTrigger
                value="apps"
                className="h-12 px-4 rounded-none data-[state=active]:border-b-2 data-[state=active]:border-primary"
              >
                <Boxes className="w-4 h-4 mr-2"/>
                性能监控
              </TabsTrigger>
              <TabsTrigger
                value="process"
                className="h-12 px-4 rounded-none data-[state=active]:border-b-2 data-[state=active]:border-primary"
              >
                <Play className="w-4 h-4 mr-2"/>
                查看任务
              </TabsTrigger>
            </TabsList>
          </div>
        </div>

        <div className="p-6">
          <div className="mx-auto">
            <TabsContent value="apps" className="m-0">
              <div className="bg-white rounded-lg p-6 shadow-sm">
                <Performance/>
              </div>
            </TabsContent>
            <TabsContent value="process" className="m-0">
              <div className="bg-white rounded-lg p-6 shadow-sm">

              </div>
            </TabsContent>
          </div>
        </div>
      </Tabs>
    </div>
  )
}

export default App
