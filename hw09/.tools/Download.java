import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.file.Files;
import java.nio.file.Path;

/** Minimal HTTPS downloader: bypasses the sandboxed schannel stack by using the JDK TLS client. */
public final class Download {

    public static void main(String[] args) throws Exception {
        if (args.length != 2) {
            System.err.println("usage: Download <url> <dest>");
            System.exit(2);
        }
        HttpClient client = HttpClient.newBuilder()
                .followRedirects(HttpClient.Redirect.ALWAYS)
                .build();
        HttpRequest request = HttpRequest.newBuilder(URI.create(args[0])).GET().build();
        HttpResponse<byte[]> response = client.send(request, HttpResponse.BodyHandlers.ofByteArray());
        if (response.statusCode() != 200) {
            throw new IllegalStateException("HTTP " + response.statusCode() + " for " + args[0]);
        }
        Path dest = Path.of(args[1]);
        Files.createDirectories(dest.getParent());
        Files.write(dest, response.body());
        System.out.println("downloaded " + Files.size(dest) + " bytes to " + dest);
    }
}
