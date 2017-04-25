Java Binary Data Deserializer
====


Requirements
----

* Jython 2.7:
```bash
cd requirements/
java -jar jython-installer-2.7.0.jar
```

* Required Jython libraries:
```bash
~/jython2.7.0/bin/pip install -r ./requirements/requirements.txt
```

Quick usage examples
----
* Deserialize Java Serialized Binary data:
```bash
CLASSPATH=./jar/*:./APP_JAR_DIRECTORY/* ~/jython2.7.0/bin/jython java_deserializer.py --deserialize -f <input_java_binary> -o <output_filename>
```

* Serialize into Java Binary data
```bash
CLASSPATH=./jar/*:./APP_JAR_DIRECTORY/* ~/jython2.7.0/bin/jython java_deserializer.py --serialize -f <input_deserialized_data> -o <output_filename>
```

References
----
https://docs.oracle.com/javase/8/docs/platform/serialization/spec/protocol.html
