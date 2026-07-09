// Engine.java

public class Engine {
    //attributes
    public String type;
    public int horsePower;
    public boolean running;

    //constructor
    public Engine(String type, int horsePower, boolean running) {
        this.type = type;
        this.horsePower = horsePower;
        this.running = running;
    }

    //methods
    public void start() {
        this.running = true;
    }

    public void stop() {
        this.running = false;
    }

    public boolean isRunning() {
        return this.running;
    }

}