import java.io.IOException;
import java.io.ObjectOutputStream;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.SocketException;

/**
 * This class works in conjunction with TcpClient.java and TcpPayload.java
 *
 * This server test class opens a socket on localhost and waits for a client
 * to connect. When a client connects, this server serializes an instance of
 * TcpPayload and sends it to the client.
 */

public class TcpServer
{
    public final static int COMM_PORT = 5050;  // socket port for client comms

    private ServerSocket serverSocket;
    private InetSocketAddress inboundAddr;
    private TcpPayload payload;

    /** Default constructor. */
    public TcpServer()
    {
        this.payload = new TcpPayload();
        initServerSocket();
        try
        {
            while (true)
            {
                // listen for and accept a client connection to serverSocket
                Socket sock = this.serverSocket.accept();
                OutputStream oStream = sock.getOutputStream();
                ObjectOutputStream ooStream = new ObjectOutputStream(oStream);
                
                ooStream.writeObject(this.payload);  // send serilized payload

                // void write(byte[] buf)
                // This method writes an array of bytes.
                byte[] bytearray = new byte[] { (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44,(byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44, (byte) 0x41, (byte)0x42, (byte)0x43, (byte)0x44};
                ooStream.write(bytearray);

                // void write(int val)
                // This method writes a byte.
                ooStream.write(5);

                // void writeBoolean(boolean val)
                //This method writes a boolean.
                ooStream.writeBoolean(true);

                // void writeByte(int val)
                // This method writes an 8 bit byte.
                ooStream.writeByte((int)100);

                // void writeBytes(String str)
                // This method writes a String as a sequence of bytes.
                //ooStream.writeBytes("writeBytes test");

                // void writeChar(int val)
                // This method writes a 16 bit char.
                ooStream.writeChar('c');

                // void writeChars(String str)
                // This method writes a String as a sequence of chars.
                //ooStream.writeChars("writeChars test");

                // void writeDouble(double val)
                // This method writes a 64 bit double.
                ooStream.writeDouble((double)55.055);

                // void writeFloat(float val)
                // This method writes a 32 bit float.
                ooStream.writeFloat((float)-90.05f);

                // void writeInt(int val)
                // This method writes a 32 bit int.
                ooStream.writeInt((int)31337);

                // void writeLong(long val)
                // This method writes a 64 bit long.
                ooStream.writeLong((long)-23895901L);

                // void writeShort(int val)
                // This method writes a 16 bit short.
                ooStream.writeShort((int)1337);

                // void writeUTF(String str)
                // This method primitive data write of this String in modified UTF-8 format.
                //ooStream.writeUTF("writeUTF test");


                //ooStream.writeInt(31337);
                ooStream.close();
                Thread.sleep(1000);
            }
        }
        catch (SecurityException se)
        {
            System.err.println("Unable to get host address due to security.");
            System.err.println(se.toString());
            System.exit(1);
        }
        catch (IOException ioe)
        {
            System.err.println("Unable to read data from an open socket.");
            System.err.println(ioe.toString());
            System.exit(1);
        }
        catch (InterruptedException ie) { }  // Thread sleep interrupted
        finally
        {
            try
            {
                this.serverSocket.close();
            }
            catch (IOException ioe)
            {
                System.err.println("Unable to close an open socket.");
                System.err.println(ioe.toString());
                System.exit(1);
            }
        }
    }

    /** Initialize a server socket for communicating with the client. */
    private void initServerSocket()
    {
        this.inboundAddr = new InetSocketAddress(COMM_PORT);
        try
        {
            this.serverSocket = new java.net.ServerSocket(COMM_PORT);
            assert this.serverSocket.isBound();
            if (this.serverSocket.isBound())
            {
                System.out.println("SERVER inbound data port " +
                    this.serverSocket.getLocalPort() +
                    " is ready and waiting for client to connect...");
            }
        }
        catch (SocketException se)
        {
            System.err.println("Unable to create socket.");
            System.err.println(se.toString());
            System.exit(1);
        }
        catch (IOException ioe)
        {
            System.err.println("Unable to read data from an open socket.");
            System.err.println(ioe.toString());
            System.exit(1);
        }
    }

    /**
     * Run this class as an application.
     */
    public static void main(String[] args)
    {
        TcpServer tcpServer = new TcpServer();
    }
}