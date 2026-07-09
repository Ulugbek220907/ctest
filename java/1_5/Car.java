public class Car {
    public static void main(String[] args) {
        Engine engine = new Engine("V8", 450, false);

        engine.start();
        System.out.println("Engine is running: " + engine.isRunning());

    }
}