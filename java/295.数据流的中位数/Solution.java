
import java.util.PriorityQueue;
import java.util.Comparator;

class MedianFinder {
    PriorityQueue<Integer> lo;
    PriorityQueue<Integer> hi;
    /** initialize your data structure here. */
    public MedianFinder() {
        Comparator<Integer> cmp = new Comparator<Integer>() {
            public int compare(Integer e1, Integer e2) {
                return e2 - e1;
            }
        };
        lo = new PriorityQueue<>();
        hi = new PriorityQueue<>(cmp);
    }

    public void addNum(int num) {
        lo.offer(num);

        hi.offer(lo.poll());
        if (hi.size() > lo.size()) {
            int mid = hi.poll();
            lo.offer(mid);
        }
    }

    public double findMedian() {
        if (lo.size() == hi.size()) 
            return ((double)lo.peek() + hi.peek()) / 2;
        else
            return (double)lo.peek();
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder(); obj.addNum(num); double param_2 =
 * obj.findMedian();
 */