class Solution {
public:
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
        int unitCount = 0;
        int remainingBox = truckSize;

        while(remainingBox > 0) {            
            int maxUnitBoxId = -1;
            int maxUnits = 0;
            for(int i=0; i<boxTypes.size(); i++){
                if(boxTypes[i][1] > maxUnits){
                    maxUnits = boxTypes[i][1];
                    maxUnitBoxId = i;
                }
            } 
            if(maxUnitBoxId == -1)
                break;
            // boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:
            int boxCount = min(remainingBox, boxTypes[maxUnitBoxId][0]);
            unitCount += boxCount*boxTypes[maxUnitBoxId][1];
            remainingBox -= boxCount;
            boxTypes[maxUnitBoxId][1] = -1;
        }
        
        return unitCount;
    }
};