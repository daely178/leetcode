
int removeDuplicates(int* nums, int numsSize){
     int *head, *tail;

    tail=head=nums+2;
    if(numsSize<=2)
        return numsSize;
    do
    {
        if(*head != *(tail-2))
        {
            *tail++ = *head;
        }

    }while(head++<(nums+numsSize-1));

    return (int)(tail-nums);
}