import java.io.Serializable;

/**
 * This class works in conjunction with TcpClient.java and TcpServer.java
 *
 * This class contains test data representing a 'payload' that is sent from
 * TcpServer to TcpClient. An object of this class is meant to be serialized by
 * the server before being sent to the client. An object of this class is meant
 * to be deserialized by the client after being received.
 */

public class TcpPayload implements Serializable
{
    // serial version UID was generated with serialver command
    static final long serialVersionUID = -50077493051991107L;

    private int int1;
    private transient int int2;  // transient members are not serialized
    private float float1;
    private double double1;
    private short short1;
    private String str1;
    private long long1;
    private char char1;

    /** Default constructor. */
    public TcpPayload()
    {
        this.int1 = 123;
        this.int2 = 456;
        this.float1 = -90.05f;
        this.double1 = 55.055;
        this.short1 = 59;
        this.str1 = "I am a String payload.";
        this.long1 = -23895901L;
        this.char1 = 'x';
    }

    /** Get a String representation of this class. */
    public String toString()
    {
        StringBuilder strB = new StringBuilder();
        strB.append("int1=" + this.int1);
        strB.append(" int2=" + this.int2);
        strB.append(" float1=" + this.float1);
        strB.append(" double1=" + this.double1);
        strB.append(" short1=" + this.short1);
        strB.append(" str1=" + this.str1);
        strB.append(" long1=" + this.long1);
        strB.append(" char1=" + this.char1);
        return strB.toString();
    }
}