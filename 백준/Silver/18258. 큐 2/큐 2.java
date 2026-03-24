import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        Queue queue = new Queue();
        for (int i = 0; i < n; i++) {
            String[] split = br.readLine().split(" ");
            switch (split[0]) {
                case "push":
                    queue.enqueue(Integer.parseInt(split[1]));
                    break;
                case "pop":
                    sb.append(queue.dequeue()).append("\n");
                    break;
                case "size":
                    sb.append(queue.size()).append("\n");
                    break;
                case "empty":
                    sb.append(queue.isEmpty() ? 1:0).append("\n");
                    break;
                case "front":
                    sb.append(queue.getFront()).append("\n");
                    break;
                case "back":
                    sb.append(queue.getRear()).append("\n");
                    break;
            }
        }
        System.out.println(sb);
    }

    public static class Node {
        private int data;
        private Node node;

        public Node(int data) {
            this.data = data;
            node = null;
        }

        public int getData() {
            return data;
        }

        public Node getNode() {
            return node;
        }

        public void setData(int data) {
            this.data = data;
        }

        public void setNode(Node node) {
            this.node = node;
        }
    }

    public static class Queue {
        private Node front;
        private Node rear;
        private int size;

        public Queue() {
            front = null;
            rear = null;
            size = 0;
        }

        public boolean isEmpty() {
            return front == null;
        }

        public void enqueue(int data) {
            Node newNode = new Node(data);
            if (rear == null) {
                front = newNode;
            }else {
                rear.node = newNode;
            }
            rear = newNode;
            size++;
        }

        public int dequeue() {
            if (isEmpty()) {
                return -1;
            }
            int temp = front.data;
            front = front.node;
            if (front == null) {
                rear = null;
            }
            size--;
            return temp;
        }

        public int size() {
            return size;
        }

        public int getFront() {
            if (isEmpty()) return -1;
            return front.data;
        }

        public int getRear() {
            if (isEmpty()) return -1;
            return rear.data;
        }
    }
}