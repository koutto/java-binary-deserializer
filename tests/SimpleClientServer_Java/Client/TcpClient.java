import java.io.IOException;
import java.io.InputStream;
import java.io.ObjectInputStream;
import java.net.Socket;
import java.net.UnknownHostException;

/**
 * TcpClient.java
 *
 * This class works in conjunction with TcpServer.java and TcpPayload.java
  *
 * This client test class connects to server class TcpServer, and in response,
* it receives a serialized an instance of TcpPayload.
 */

public class TcpClient
{
    public final static String SERVER_HOSTNAME = "192.168.142.160";
    public final static int COMM_PORT = 5050;  // socket port for client comms

    private Socket socket;
    private TcpPayload payload;
    private byte[] recv1;
    private byte recv2;
    private boolean recv3;
    private byte recv4;
    private byte[] recv5;
    private char recv6;
    private byte[] recv7;
    private double recv8;
    private float recv9;
    private int recv10;
    private long recv11;
    private short recv12;

    /** Default constructor. */
    public TcpClient()
    {
        try
        {
            this.socket = new Socket(SERVER_HOSTNAME, COMM_PORT);
            InputStream iStream = this.socket.getInputStream();
            ObjectInputStream oiStream = new ObjectInputStream(iStream);
            this.payload = (TcpPayload) oiStream.readObject();

            this.recv1 = new byte[4];
            oiStream.read(this.recv1, 0, 4);

            this.recv2 = oiStream.readByte();

            this.recv3 = oiStream.readBoolean();

            this.recv4 = oiStream.readByte();

            //this.recv5 = 

            this.recv6 = oiStream.readChar();

            //this.recv7 = 

            this.recv8 = oiStream.readDouble();

            this.recv9 = oiStream.readFloat();

            this.recv10 = oiStream.readInt();

            this.recv11 = oiStream.readLong();

            this.recv12 = oiStream.readShort();

            //this.recv13 = 

        }
        catch (UnknownHostException uhe)
        {
            System.out.println("Don't know about host: " + SERVER_HOSTNAME);
            System.exit(1);
        }
        catch (IOException ioe)
        {
            System.out.println("Couldn't get I/O for the connection to: " +
                SERVER_HOSTNAME + ":" + COMM_PORT);
            System.exit(1);
        }
        catch(ClassNotFoundException cne)
        {
            System.out.println("Wanted class TcpPayload, but got class " + cne);
        }
        System.out.println("Received payload:");
        System.out.println(this.payload.toString());
        System.out.println(this.recv1);
        System.out.println(this.recv2);
        System.out.println(this.recv3);
        System.out.println(this.recv4);

        System.out.println(this.recv6);

        System.out.println(this.recv8);
        System.out.println(this.recv9);
        System.out.println(this.recv10);
        System.out.println(this.recv11);
        System.out.println(this.recv12);

    }

    /**
     * Run this class as an application.
     */
    public static void main(String[] args)
    {
        TcpClient tcpclient = new TcpClient();
    }
}
